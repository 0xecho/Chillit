# Chillit
`Chill-it` is a simple python tool you can add to your workflow to limit the number of time you request data to the same host without losing efficiency or having to edit every tool to do the same thing.

## Installation

Just clone this repo and call the chillit.py file
```bash
git clone https://github.com/0xecho/Chillit.git
cd Chillit
```

## Usage
The usage is pretty simple, it takes input from stdin and outputs urls with a delay of 3 seconds b/n similar hosts. (Too lazy to add argparse to customize the number of seconds to delay)
```
cat domains | python3 /path/to/chillit.py | httpx
```

## TODO

- [ ] Add arguments support [delay b/n similar hosts] 
- [ ] Add support for delaying `x requests every x seconds` instead of just `1 request every x seconds`

## Contributing
Pull requests are always **welcome**. For major changes, please open an issue first to discuss what you would like to change.

## License
I don't believe in licensing code. GO NUTS!!!
