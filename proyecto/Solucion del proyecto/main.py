import pandas as pd
from sub_modules import congfig_parser

def inicialize(logger,*args):
    try:
        inventario = pd.read_csv(args[0]['inventory'],
                                 usecols=[int(x) for x in args[0]['inventory_columns'].splitlines()],
                                 names=args[0]['inventory_columns_names'].splitlines(),
                                 header=0)
        logger.info(f' Inventory successfully  loaded, {str(len(inventario))} items in inventory')
        for index,item in inventario.iterrows():
            print(f'Col# {str(index)} {item["IP"]} - {item["Tipo"]}')
    except Exception as e:
        logger.error(f' Unable to import inventory, {e}')
        
if __name__ == '__main__':
    try:
        config_files = congfig_parser.get_config_files('./configs/app_config.cfg','env')

        logger = congfig_parser.log_parser(config_files['logging_configs'])
        inicialize(logger,config_files,{'oragm':'red'})
    except Exception as e:
        logger.error(f' An error occured during the execution of the script exiting routine {e}')
        