import matplotlib.pyplot as plt

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

def groupby_count_head(df,column_name,count_column_name):
    return df.groupby(column_name)[count_column_name].count().reset_index().sort_values(by = count_column_name, ascending=False, ignore_index=True).head()

def top_5_bar_plot(df, column_name, count_column_name, x_label, y_label, title, image_name):
    fig, ax = plt.subplots(figsize=(8, 4))
    top_5 = groupby_count_head(df, column_name, count_column_name)
    for label, df in top_5.groupby(column_name):
        ax.bar(df[column_name], df[count_column_name], label=label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend(title=column_name)
    plt.savefig(f"../images/{image_name}.png")
    plt.show()

def top_bottom_5_bar_plot(df,column_name,x_label,y_label,title,image_name):
    # Group by department and count the number of sales, then sort in descending order
    sales_by_column = df.groupby(column_name).size().sort_values(ascending=False)
    
    # Bar plot for visualization
    plt.figure(figsize=(12, 6))
    
    # Plotting top departments
    plt.subplot(1, 2, 1)
    plt.bar(sales_by_column.index[:5], sales_by_column.values[:5], color='green')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'Top {title}')
    plt.xticks(rotation=45)
    
    # Plotting bottom departments
    plt.subplot(1, 2, 2)
    plt.bar(sales_by_column.index[-5:], sales_by_column.values[-5:], color='orange')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'Bottom {title}')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig(f"../images/{image_name}.png")
    plt.show()