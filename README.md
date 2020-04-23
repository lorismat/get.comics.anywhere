# get.comics.anywhere

`get-comics-anywhere` is a CLI app which can be run on any UNIX system with the required dependencies.  
With the app, you can download chapters from any comics available on the [comicextra.com](https://www.comicextra.com/) website.  
Below is a quick demo with a set of useful commands:
- `get-comics -h` will give you the list of available commands
- `get-comics "Comic Title"` will prompt you to enter a chapter, and download it as a .zip file
- `get-comics -a` will list all available titles
- `get-comics -l W` will list all available titles starting with the letter `W`  


<p style="text-align:center;"><img src="gif-get-comics.gif" style="border-radius:15px;" /></p> 


**Compatible with UNIX system only (Linux, macOS)** 

## How to download

### Download with pip

`pip3 install `  

### Download from source code

Feel free to clone this repository.  
From the root of the repository, run:  
```
sudo sh install.sh
```  
You will be able to run the CLI app from anywhere in the terminal, with `get-comics`.  

#### To uninstall the app:  
```
pip3 uninstall get-comics
```   

## Requirements

**[Ubuntu Users]**  
To be able to execute the newly downloaded package from the command line, make sure you added:  
`export PATH=$PATH:~/.local/bin` to your `.bashrc` file

### Selenium

Selenium is a tool simulating a browser to access elements of a page. It is really useful in many fields of web development. It is used in this package, and you will have to install it and set it up, as follow:  

- install it with:  
	`pip3 install selenium`

- set it up with a specific driver:  

To make `selenium` usable, you have to download a specific `geckodriver`.  
1. Download [latest version of the gecko driver](https://github.com/mozilla/geckodriver/releases) depending on your system
2. Unzip/untar the file  
	`tar xzf you_geckodriver_tar_file`  
3. In your `.bashrc` file (Linux), or `.bash_profile` file (macOS), set up the path:  
`export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step`  

You can now run the CLI app from anywhere with `get-comics` and specific options!  

# Documentation

## Structure of the repository


