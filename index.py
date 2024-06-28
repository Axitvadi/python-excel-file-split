import pandas as pd
import os


def split_excel(fileName, chunk_size, folder_name, columns_to_remove):
    # Read the large Excel file in chunks
    current_dir = os.path.dirname(__file__)

    # Build the full file path
    file_path = os.path.join(current_dir, fileName)
    save_file_path = os.path.join(current_dir, folder_name)

    chunk_iterator = pd.read_csv(file_path, chunksize=chunk_size)

    for i, chunk in enumerate(chunk_iterator):
         # Drop the specified columns
        chunk.drop(columns = columns_to_remove, inplace=True)

        output_file_path = os.path.join(save_file_path, f"{os.path.splitext(fileName)[0]}_chunk_{i+1}.xlsx")
        chunk.to_excel(output_file_path, index=False, engine='openpyxl')
        print(f"Saved chunk {i + 1} to {output_file_path}")

# Parameters
file_path = 'EuroData.csv'
chunk_size = 100000  # Adjust this value based on your memory constraints
folder_name = 'OUT'
columns_to_remove = [ "FREQ", "REF_AREA", "PROVIDER_FM", "INSTRUMENT_FM", "PROVIDER_FM_ID", "DATA_TYPE_FM", "OBS_STATUS", "OBS_CONF", "OBS_PRE_BREAK", "OBS_COM", "TIME_FORMAT","BREAKS", "COLLECTION","COMPILING_ORG", "DISS_ORG", "DOM_SER_IDS", "FM_CONTRACT_TIME", "FM_COUPON_RATE", "FM_IDENTIFIER", "FM_LOT_SIZE", "FM_MATURITY", "FM_OUTS_AMOUNT", "FM_PUT_CALL", "FM_STRIKE_PRICE", "PUBL_MU", "PUBL_PUBLIC", "UNIT_INDEX_BASE", "COMPILATION", "COVERAGE", "DECIMALS", "SOURCE_AGENCY", "SOURCE_PUB", "UNIT_MULT" ]

# Run the split function
split_excel(file_path, chunk_size, folder_name, columns_to_remove)
