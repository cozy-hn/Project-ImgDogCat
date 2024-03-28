# Project-ImgDogCat
This repository contains a program designed to display random images of dogs and cats within iTerm2, utilizing the imgcat script for seamless integration. Ideal for pet lovers and developers looking for a touch of whimsy in their terminal sessions.

# Example

<img width="332" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/66d53b11-df14-4e13-ac95-80ff0fc814ff">
<img width="410" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/adf32458-5945-486d-983e-15bf72c49e30">
<img width="357" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/c418c4a6-c562-4155-bd2c-5dbcb0395229">
<img width="400" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/11faeed2-7049-422d-8d96-a2ef1d9a4a0d">

# How to download

### For M1
```bash
cd ~ && mkdir -p imgdogcat && cd imgdogcat && curl -L -O https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.3.0/imgcat.sh && curl -L -o imgdogcat https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.3.0/imgdogcat_m1 && chmod +x imgdogcat imgcat.sh
```

### For x86
```bash
cd ~ && mkdir -p imgdogcat && cd imgdogcat && curl -L -O https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.3.0/imgcat.sh && curl -L -o imgdogcat https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.3.0/imgdogcat_intelx86 && chmod +x imgdogcat imgcat.sh
```

## Useful alias examples

```bash
alias bark='~/imgdogcat/imgdogcat --dog'
alias meow='~/imgdogcat/imgdogcat --cat'
alias gg='~/imgdogcat/imgdogcat --gif'
```

## imgdogcat v0.3.1

We are thrilled to present the release of imgdogcat v0.3.0, tailored for developers and animal enthusiasts. This innovative feature allows users to randomly display cat or dog images in their terminal, offering a delightful and refreshing break during coding sessions.

## Features

- `--cat`, `-c` option: Show a random cat picture.
- `--dog`, `-d` option: Show a random dog picture.
- `--gif`, `-g` option: Show a random k-pop gif.
- `--api`, `-a` option: you can use your own api key to get the gif from giphy.
- `--search`, `-s` option: Show a random gif with searched category
- `--help`, `-h` option: Display help information.
- No specific option: Randomly displays a cat or dog picture.

## Compatibility and Requirements

- **Platform Compatibility**: Two binary files are provided with this release:
    - `imgcat_intelx86` is built for Macs using Intel architecture.
    - `imgcat_m1` is built for Macs with M1 architecture.
  Please download the binary corresponding to your machine's architecture.

- **Terminal Compatibility**: This tool is optimized for use in iTerm2 with the `imgcat` feature. For the best experience, please use iTerm2 as your terminal. Make sure that both the executable file and the `imgcat.sh` script are located in the same directory.

## Using imgdogcat in VSCode Terminal

To properly use imgdogcat in the Visual Studio Code terminal and display images directly, you must enable the option to support images within VSCode settings. Follow these steps to enable image support:

1. Open Visual Studio Code.
2. Go to `File > Preferences > Settings` (or `Code > Preferences > Settings` on Mac).
3. In the search bar at the top, type `Terminal > Integrated: Enable Images`.
4. Find the setting labeled **Enable Images** under the section **Terminal > Integrated**.
5. Check the box next to **Enable Images** to allow images to be displayed in the terminal.
6. Restart VSCode for the changes to take effect.

<img width="491" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/3da355aa-323a-4032-b217-1594f566e483">

- Once you've enabled this option, you should be able to use imgdogcat in your VSCode terminal and see images directly in the output.
- But gif images are not supported in the VSCode terminal. 🥲


## Installation

1. Download the appropriate binary for your architecture.
2. Ensure you have the `imgcat.sh` script in the same directory as the downloaded binary.
3. Change the permissions to allow execution of the binary:

    ```bash
    chmod +x imgdogcat_m1 imgdogcat_intelx86 imgcat.sh
    ```

## Usage

Execute the binary with your choice of option:

```bash
./imgdogcat --cat   # Displays a random cat image
./imgdogcat --dog   # Displays a random dog image
./imgdogcat --gif  # Displays a random gif image
./imgdogcat --search # Displays a random gif image within searched category
./imgdogcat --api <your_api_key> --gif # Displays a random gif image with your own api key
./imgdogcat         # Randomly displays a cat or dog image
```

## Feedback

Your feedback is highly appreciated! If you encounter any issues or have suggestions for improvement, please open an issue on our GitHub repository. Let's make imgdogcat better together!

Thank you for using imgdogcat, and enjoy the cute overload!
