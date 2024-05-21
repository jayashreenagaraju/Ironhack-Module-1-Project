def print_in_red(data):
    # ANSI escape code for red color
    red_color = "\033[91m"
    # ANSI escape code to reset color
    reset_color = "\033[0m"

    print(red_color + data + reset_color)


def clean_column_names(df):
    df.rename(columns = {col:col.strip().lower().replace(' ','_') for col in df.columns},inplace=True)


def drop_columns(df, columns_list):
    df.drop(columns = columns_list, inplace=True)


def fillna_col(df, column, na_value_replace):
    return df[column].fillna(na_value_replace)