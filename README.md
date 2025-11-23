# Coffee Shop CLI Application

This is a simple command-line interface (CLI) application for managing a coffee shop's orders, customers, and coffee types. It's built with Python and demonstrates object-oriented programming (OOP) principles and relationships between different data models.

## Table of Contents

- [Features](#features)
- [Models](#models)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create and manage customers.
- Create and manage coffee types.
- Create orders that link customers and coffees.
- View relationships, such as all orders for a customer or all customers who have ordered a specific coffee.
- Calculate aggregate data, like the average price of a coffee or the customer who has spent the most on a particular coffee.

## Models

The application is built around three main models:

### `Customer`

- `name`: `string` (must be between 1 and 15 characters)
- `orders()`: Returns a list of all orders placed by the customer.
- `coffees()`: Returns a unique list of all coffees the customer has ordered.
- `create_order(coffee, price)`: Creates a new order for the customer.

### `Coffee`

- `name`: `string` (must be at least 3 characters, cannot be changed after creation)
- `orders()`: Returns a list of all orders for this coffee.
- `customers()`: Returns a unique list of all customers who have ordered this coffee.
- `num_orders()`: Returns the total number of times this coffee has been ordered.
- `average_price()`: Returns the average price of this coffee across all its orders.

### `Order`

- `customer`: `Customer` instance
- `coffee`: `Coffee` instance
- `price`: `float` (must be between 1.0 and 10.0)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3 and `pipenv` installed.

### Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone https://github.com/pyrxallan/coffee_shop.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd coffee_shop
    ```
3.  Install the required dependencies using `pipenv`:
    ```bash
    pipenv install
    ```
4.  Activate the virtual environment:
    ```bash
    pipenv shell
    ```

## Usage

The `debug.py` script is provided to demonstrate the functionality of the models and their interactions. It creates instances of coffees and customers, simulates orders, and prints out the results of various methods.

To run the debug script:
```bash
python debug.py
```
This will also start an `ipdb` session, allowing you to interactively inspect the objects and test the methods.

## Project Structure

```
/coffee_shop
├── coffee.py
├── customer.py
├── debug.py
├── order.py
├── Pipfile             # Project dependencies
├── Pipfile.lock
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.