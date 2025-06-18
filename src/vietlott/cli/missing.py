import math

import click
import pandas as pd
import pendulum
from loguru import logger

from vietlott.config.map_class import map_class_name
from vietlott.config.products import ProductConfig, product_config_map
from vietlott.crawler.products import BaseProduct


@click.command()
@click.pass_context
@click.argument("product")
@click.option("--limit", default=20)
def detect_missing_data(ctx, product, limit):
    """
    detect_missing_data and run if needed
    :param ctx: context
    :param product: product to run
    :param limit: number of pages to run
    :return:
    """
    # Exclude bingo18 from missing data detection
    if product == "bingo18":
        logger.warning("Bingo18 is currently excluded from missing data detection")
        return
    
    logger.info(f"Starting missing data detection for product: {product}")
    
    try:
        if product not in product_config_map:
            click.echo(f"Error:: Product must in product_map: {list(product_config_map.keys())}", err=True)
            ctx.exit(1)
        click.echo(f"product={product}, limit={limit}")

        product_cfg: ProductConfig = product_config_map[product]
        df = pd.read_json(product_cfg.raw_path, lines=True)
        print(df["id"].dtype)
        if df["id"].dtype == "object":
            df["id"] = df["id"].str.replace("#", "").astype(int)
        df["id_next"] = df["id"].shift(-1)
        df["diff"] = df["id_next"] - df["id"]

        df_missing = df[df["diff"] > 1]
        last_id = df["id"].max()
        df_missing["index"] = df_missing["id"].apply(lambda x: (last_id - x) / product_cfg.page_size)
        df_missing["index_next"] = df_missing["id_next"].apply(lambda x: (last_id - x) / product_cfg.page_size)
        df_missing_process = df_missing.iloc[::-1].iloc[1:].head(limit)

        logger.info("\n" + df_missing_process[["date", "id", "id_next", "diff", "index", "index_next"]].to_markdown())

        run_date = pendulum.now(tz="Asia/Ho_Chi_Minh").to_date_string()
        product_obj: BaseProduct = map_class_name[product]()
        for row in df_missing_process.itertuples():
            if (row.index - row.index_next) > 50:
                step = 20
                for i in range(int(math.floor(row.index_next)), int(math.ceil(row.index)), step):
                    product_obj.crawl(
                        run_date_str=run_date,
                        index_from=i,
                        index_to=i + step,
                    )
            else:
                product_obj.crawl(
                    run_date_str=run_date,
                    index_from=int(math.floor(row.index_next)),
                    index_to=int(math.ceil(row.index)),
                )

        logger.info(f"Successfully detected missing data for {product}")
    except Exception as e:
        logger.error(f"Error detecting missing data for {product}: {e}")
        raise


if __name__ == "__main__":
    detect_missing_data()
