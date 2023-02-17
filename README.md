# Project Euler

Welcome to the Project Euler repository! This repository contains solutions to the problems posed on the Project Euler website. The solutions are explained in the [TurtleSmoke Project Euler](https://turtlesmoke.github.io/Project-Euler/) website.

## Contributing

If you would like to contribute to this repository, please consult the [CONTRIBUTING.md](./CONTRIBUTING.md) file for guidelines on how to do so.

While there are no specific rules regarding the code base, it is essential that the code is understandable and not an incomprehensible one-liner. The primary goal is clarity, not performance. Please note that pull requests may be rejected if the proposed changes are deemed uninteresting.

## Running the server

To run the website locally, you will need to download [mdbook](https://rust-lang.github.io/mdBook/).

Once mdbook is installed, you can start the server using the following command:

```shell
mdbook serve
```

The server will then be accessible at `localhost:3000`. If necessary, you can update the `book.toml` configuration files to suit your needs.

## Scripts

All utility scripts can be found in the `scripts` folder. Here is a brief description of each script:

- `run_black.sh`: Runs black on all python files.
- `run_pylint.sh`: Runs pylint on all python files.
- `generate_problem.sh`: Generates python/markdown files for a new exercise solution.
- `remove_problem.sh`: Reverses the changes made by `generate_problem.sh`.
- `generate_example.py`: Generates code samples for markdown explanations.
- `remove_example.py`: Replaces the changes made by `generate_example.py` with the template code.
