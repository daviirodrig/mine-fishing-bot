# mine-fishing-bot

This python script farm treasures from fishing automatically in Minecraft by reading the subtitles in the screen.

## Installation

- Install dependencies from Pypi with pip:

  ```sh
  $ pip install -r requirements.txt
  ```

### Minecraft Settings

For this script to work with Minecraft you have to make sure that `Raw Input` is disabled in your Minecraft settings.

Also, make sure subtitles are enabled on audio settings.

## Usage

Start the script with `python main.py`.

After that, go to Minecraft and throw the bobber in the water, the script should right-click automatically when the fish is caught and the subtitle `Fishing Bobber Splashes` appears.

You can change the subtitle image to find in the script, accordingly to your resolution

The tested resolutions are:

- 1920x1080 - `images/subtitle.png`
- 1366x768 - `images/subtitle3.png`

For better usage of the script you should take your own screenshot of the `Fishing Bobber Splashes`, add to the images folder and update the script accordingly.
