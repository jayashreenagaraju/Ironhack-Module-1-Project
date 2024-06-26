# Walmart Grocery Sales Analysis

## Project Overview
This project analyzes product information from Walmart's Grocery department. The dataset includes details such as prices, sizes, promotions, and product URLs. The analysis aims to uncover insights into pricing and sales distributions across different brands, categories, and departments.

## Dataset

Dataset can be found [here](https://www.kaggle.com/datasets/thedevastator/product-prices-and-sizes-from-walmart-grocery)

The dataset includes product information such as prices, sizes, promotions, and product URLs. Key columns are:

- `SHIPPING_LOCATION`: The location from where the product is shipped.
- `DEPARTMENT`: The department in which the product is categorized.
- `CATEGORY`: The category in which the product is categorized.
- `SUBCATEGORY`: The subcategory in which the product is categorized.
- `BREADCRUMBS`: Breadcrumbs for the product (Linking information of a product department/category/subcategory).
- `SKU`: SKU for the product (SKU stands for Stock-keeping unit. A Product SKU is a string representing the Product unique identifier in an Ecommerce shop).
- `PRODUCT_URL`: URL for the product.
- `PRODUCT_NAME`: Name of the product.
- `BRAND`: Brand of the product.
- `PRICE_RETAIL`: Retail price of the product.
- `PRICE_CURRENT`: Current price of the product.
- `PRODUCT_SIZE`: Size of the product.
- `PROMOTION`: Promotion for the product.
- `RunDate`: Date on which the data was collected.

## Project Steps

1. **Setup**
    - Imported necessary libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`.
    - Loaded the dataset using YAML configuration.
    - Created `function.py` to have functions for code reusability

2. **Data Cleaning and Preprocessing**
    - Printed information and shape of the dataframe.
    - Renamed columns for clarity.
    - Dropped irrelevant columns.
    - Checked and handled null values by replacing NaNs with readable values.
    - Standardized the date format in the `RunDate` column.


3. **Exploratory Data Analysis (EDA)**              
The EDA involves:
    - Grouping by brand to calculate the average current price.
    - Grouping by category to calculate the total sales (sum of current prices).
    - Counting the number of products per brand and per department.
    - Finding the unique count of subcategories for each department.
    - Grouped by brand and subcategory to get unique product sizes sold.
      
4. **Hypotheses and Visualizations**      
The hypotheses tested and corresponding visualizations include:

    - **Sales Analysis**:
        - Group by brand, department, category, and product name to count the total number of sales and display the top and bottom 5 in bar graphs.
    - **Price Analysis**:
        - Check if `price_retail` is the same as `price_current`.
        - Create a `discount` column to the data frame and create a new discount data frame for further analysis
    - **Discount Analysis**:
        - Bar plots for the top 5 brands, departments, categories, and products on discount.
    - **Sales Distribution**:
        - Count the total number of sales by brand, department, and category, displaying them by percentage.
    - **Revenue Analysis**:
        - Aggregate by `price_current` and group by necessary columns to calculate total revenue.
        - Show bar charts of the highest and lowest revenue by brands.

## Visualizations
FYI: Bar graphs are in skyblue color for top line and grey for bottom line
- Bar graphs showing top and bottom entities (brands, departments, categories, products) by sales.
- Bar graphs illustrating the impact of discounts.
- Percentage distributions of sales by brand, department and category.
- Revenue bar charts highlighting financial performance by brand.

## Results & Insights
**Brand Performance**: The analysis of sales distribution by brand can help Walmart identify which brands are performing well and which ones need attention. This can inform stocking decisions, marketing strategies, and partnership evaluations.

**Department and Category Trends**: Understanding sales patterns across departments and categories allows for better inventory management and promotional strategies tailored to customer demand.

**Effectiveness of Promotions**: By analyzing discounts and their impact on sales, Walmart can optimize their promotional efforts to maximize revenue and customer satisfaction.

**Product Popularity**: Insights into the most and least popular products can guide product development, discontinuation decisions, and targeted marketing campaigns.


## Conclusion
The comprehensive analysis of Walmart's Grocery department sales data reveals significant trends in brand performance, departmental sales, and the impact of pricing and promotions on consumer behavior. These insights can be leveraged to enhance strategic decision-making, optimize inventory and promotions, and ultimately improve overall business performance. The visualizations and findings presented in this project provide a valuable resource for understanding and addressing key factors that drive sales and customer satisfaction at Walmart.