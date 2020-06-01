# YSCounter
YouTube Subscriber Counter with Arduino and Python (Without API key). Scrape Live subscriber Counter data from the [Social Blade](https://socialblade.com) website and display it on a 2X16 LCD screen using Arduino. You don't need the *YouTube API key* to do this.

Visit my friend's YouTube channel! <br/>
**Nepercos**: [youtube.com/nepercos](https://youtube.com/nepercos)

### Availability
Only GNU/Linux

## Requirements
- Arduino (Preferably the *Uno* model)
- Serial port cable
- 2x16 LCD Screen
- 10K resistor or 10K potentiometer
- 18 jumper cables
- Breadboard to test

Circuit Diagrams:

<img src="">
<img src="">

## Installing
```sh
git clone https://github.com/adlgrbz/yscounter
```

Install via Python:
```sh
cd yscounter
python3 setup.py build && [sudo] python3 setup.py install
```

## Usage
**1.** Open the software.

```sh
yscounter
```

or `Application Menu` > `Utility` > `YSCounter`

**2.** Enter your YouTube channel ID.

How to find a channel ID?
![]()

**3.** Choose the Arduino port.

**4.** Upload the code to the Arduino card.

**5.** Test the subscriber data.

**6.** Send the data to the card.

## Demo

![]()

## Contributors

<table><tr><td align="center"><a href="https://github.com/GizliProfesor"><img src="https://avatars2.githubusercontent.com/u/44980977?s=460&u=144b3b380716233f08f94f31cb06f2899b86e9fb&v=4" width="100px;" alt=""><br/><sub>GizliProfesor</b></sub></a><br/></td></tr></table>

## License
This project is licensed under the GNU GPL v3 License - see the [LICENSE](LICENSE) file for details