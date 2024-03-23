# Project-ImgDogCat
This repository contains a program designed to display random images of dogs and cats within iTerm2, utilizing the imgcat script for seamless integration. Ideal for pet lovers and developers looking for a touch of whimsy in their terminal sessions.

# Example

<img width="332" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/66d53b11-df14-4e13-ac95-80ff0fc814ff">
<img width="410" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/adf32458-5945-486d-983e-15bf72c49e30">
<img width="357" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/c418c4a6-c562-4155-bd2c-5dbcb0395229">
<img width="400" alt="image" src="https://github.com/cozy-hn/Project-ImgDogCat/assets/110678456/11faeed2-7049-422d-8d96-a2ef1d9a4a0d">

# How to use

### For M1
```bash
curl -L -O https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.1.0/imgcat.sh && curl -L -o imgdogcat https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.1.0/imgdogcat_m1 &&  chmod +x imgdogcat imgcat.sh
```

### For x86
```bash
curl -L -O https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.1.0/imgcat.sh && curl -L -o imgdogcat https://github.com/cozy-hn/Project-ImgDogCat/releases/download/v0.1.0/imgdogcat_intelx86 && chmod +x imgdogcat imgcat.sh
```

## imgdogcat v0.1.0

We are thrilled to present the release of imgdogcat v0.1.0, tailored for developers and animal enthusiasts. This innovative feature allows users to randomly display cat or dog images in their terminal, offering a delightful and refreshing break during coding sessions.

## Features

- `--cat`, `-c` option: Show a random cat picture.
- `--dog`, `-d` option: Show a random dog picture.
- No specific option: Randomly displays a cat or dog picture.

## Compatibility and Requirements

- **Platform Compatibility**: Two binary files are provided with this release:
    - `imgcat_intelx86` is built for Macs using Intel architecture.
    - `imgcat_m1` is built for Macs with M1 architecture.
  Please download the binary corresponding to your machine's architecture.

- **Terminal Compatibility**: This tool is optimized for use in iTerm2 with the `imgcat` feature. For the best experience, please use iTerm2 as your terminal. Make sure that both the executable file and the `imgcat.sh` script are located in the same directory.

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
./imgdogcat         # Randomly displays a cat or dog image
```

## Feedback

Your feedback is highly appreciated! If you encounter any issues or have suggestions for improvement, please open an issue on our GitHub repository. Let's make imgdogcat better together!

Thank you for using imgdogcat, and enjoy the cute overload!
