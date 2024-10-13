# Web Scraping MorphMarket

This script scrapes product details from the MorphMarket website and saves the data into a CSV file.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- pandas
- webdriver_manager

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:

```sh
pip install selenium beautifulsoup4 pandas webdriver_manager
```

## Usage

1. Open the script and configure the initial settings if necessary.
2. Run the script:

```sh
python webscraping.py
```

## Script Details

### Initial Configuration

- **URL**: The base URL of the MorphMarket website.
- **Headers**: User-Agent headers to mimic a real browser.
- **WebDriver Options**: Chrome options to configure the WebDriver.

### Data Structure

A dictionary [`dic_produtos`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A0%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition") is used to store the scraped data with the following keys:
- [`marca`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A40%2C%22character%22%3A12%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition"): Brand name
- [`preco`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A41%2C%22character%22%3A12%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition"): Price
- [`sexo`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A63%2C%22character%22%3A12%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition"): Sex
- [`traits`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A68%2C%22character%22%3A12%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition"): Traits
- [`origem`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A73%2C%22character%22%3A12%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition"): Origin
- [`nascimento`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A78%2C%22character%22%3A12%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition"): Birth date
- [`link`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A101%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition"): Product link

### Scraping Process

1. **Iterate over multiple pages**: The script iterates over multiple pages of product listings.
2. **Access each page**: For each page, the script accesses the URL and waits for the page to load.
3. **Parse the page**: The page source is parsed using BeautifulSoup.
4. **Find products**: The script finds all product elements on the page.
5. **Extract product details**: For each product, the script extracts the brand name, price, and product link.
6. **Access product details page**: The script accesses the product details page and extracts additional information such as sex, traits, origin, and birth date.
7. **Store the results**: The extracted data is stored in the [`dic_produtos`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fgeorge%2FDesktop%2FPython2024Prog%2Fwebscraping.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22X56sZmlsZQ%3D%3D%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A0%7D%7D%5D%2C%227f2c1b18-4c41-40c8-85db-53ea3dc0893c%22%5D "Go to definition") dictionary.

### Save Results

After scraping, the script saves the results to a CSV file named `detalhes_produtos.csv`.

## Debugging

The script includes several print statements for debugging purposes:
- Print the current page being accessed.
- Print a message if no products are found on a page.
- Print each product found with its details.
- Print a message before saving the results to a CSV file.

## Notes

- Adjust the range in the for loop to scrape more pages.
- Ensure that the WebDriver is properly installed and configured.
- Modify the script as needed to handle any changes in the website's structure.

## License

This project is licensed under the MIT License.
