# Dressmaker Measurement Book App

## MBook Console

The MBook Console is a command-line interface (CLI) designed to interact with the MBook application. It provides a set of commands to create, display, and manage instances of different classes such as User and Customer.

### Getting Started

#### Prerequisites

- Python 3.x
- Required Python modules (listed in `requirements.txt`)

#### Installation

1. Clone the repository to your local machine:

    `git clone https://github.com/Maneida/dressmaker_measurement_book_app.git`

2. Navigate to the project directory:

    `cd mbook-console`

3. Install the required dependencies:

    `pip install -r requirements.txt`

### Usage

To run the MBook Console, use the following command:

`python mbook_console.py`

#### Commands

- `create <class_name> [attribute=value ...]`: Create a new instance of the specified class. You can provide attributes and their values in the format `attribute=value`.

- `show <class_name> [attribute] [value]`: Display an instance of the specified class. If attributes and values are provided, it will search for instances with matching attributes.

- `destroy <class_name> <instance_id>`: Delete an instance based on its class name and ID.

- `all [class_name] [attribute] [value]`: Display string representations of instances. If attributes and values are provided, it will search for instances with matching attributes.

- `update <class_name> <instance_id> <attribute> <value>`: Update an instance's attribute with the provided value.

- `count <class_name>`: Count the number of instances of a class.

- `quit` or `exit`: Exit the MBook Console.

#### Examples

1. Create a User:

    `create User first_name="Alice" surname="Johnson" email="alice@example.com" password="password123"`

2. Show a Customer with a specific user_id:

    `show Customer user_id="f6bd9fe8-27d8-4976-ac5e-ecfb654bd289"`

3. Update a User's email:

    `update User f6bd9fe8-27d8-4976-ac5e-ecfb654bd289 email "alice.j@example.com"`

4. Count the number of Customers:

    `count Customer`

### Contributing

If you'd like to contribute to the MBook Console, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

### Authors

Michael Amuah - [Github](https://github.com/maneida) / [Twitter](https://twitter.com/kayku_d)  

### License

This project is licensed under the [MIT License](LICENSE).
