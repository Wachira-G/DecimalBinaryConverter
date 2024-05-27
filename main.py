#!/usr/bin/env python3

"""A simple decimal to binary and binary to decimal converter app built with Kivy and KivyMD.

This app allows users to convert between decimal and binary representations of numbers.
"""

import kivy
import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

Builder.load_file('main.kv')


class Converter(MDScreen):
    """Converter app main functionality.

    This class handles the core logic of the converter app, including switching
    between conversion modes (decimal to binary and vice versa), performing the
    conversion calculations, and updating the UI elements.
    """

    state = 0  # Dec to Bin. State 1 is Bin to Dec

    def flip(self):
        """Flip app states into binary to decimal conversion and vice versa.

        This method resets the UI elements (result text, label text, and input hint)
        and updates the app title and input hint text based on the current state.
        """
        self.ids.result.text = ''
        self.ids.label.text = ''
        self.ids.input_text_hint.text = ''

        if self.state == 0:
            self.state = 1
            # app title
            self.ids.title.text = 'Binary to Decimal Converter'
            # textfield text
            self.ids.input_text_hint.text = 'Enter a binary number'
        else:
            self.state = 0
            # app title
            self.ids.title.text = 'Decimal to Binary Converter'
            # textfield text
            self.ids.input_text_hint.text = 'Enter a decimal number'

    @staticmethod
    def bin2dec(binary):
        """Convert a binary representation number (string) into a decimal number (string).

        This method handles both integer and floating-point binary representations.
        It validates the input to ensure it's a valid binary number,
        (containing only 0s and 1s).

        Args:
            binary: The binary representation of the number as a string.

        Returns:
            The converted decimal number as a string.
            Raises a ValueError if the input is invalid.
        """

        if not all(char in '01' for char in binary):
            raise ValueError("Invalid binary input. Please enter only 0s and 1s.")

        # floats
        if '.' in binary:
            whole, fract = binary.split('.')
            whole = int(whole, 2)
            floating = 0
            for idx, digit in enumerate(fract):
                floating += int(digit) * 2 ** (-(idx + 1))
            dec = str(whole + floating)

        # ints
        else:
            dec = str(int(binary, 2))
        return dec

    @staticmethod
    def dec2bin(dec: str)->str:
        """Convert a decimal number (string) into a binary representation (string).

        This method handles both integer and floating-point decimal numbers.
        It uses a loop with a limited number of iterations to avoid potential endless loops
        when converting floating-point numbers.

        Args:
            dec: The decimal number as a string.

        Returns:
            The converted binary representation as a string.
        """
        # floats
        if '.' in dec:
            whole, fract = dec.split('.')
            decimal_places = 10  # Limit iterations to avoid endless loop
            whole = bin(int(whole))[2:]
            fract = float('0.' + fract)
            floating = []
            for i in range(decimal_places):
                if fract * 2 < 1:
                    floating .append('0')
                    fract *= 2
                elif fract * 2 > 1:
                    floating.append('1')
                    fract = fract * 2 - 1
                elif fract * 2 == 1.0:
                    floating.append('1')
                    break
            binary = whole + '.' + ''.join(floating)

        # ints
        else:
            binary = bin(int(dec))[2:]
        return binary

    def convert(self):
        """Perform the conversion based on the current state and update the UI.

        This method retrieves the user input,
        checks for validity based on the current state (decimal or binary),
        performs the conversion using the appropriate method (bin2dec or dec2bin),
        and updates the label and result text fields with the converted value
        and a descriptive label.
        It also includes error handling
        to catch potential ValueErrors during conversion
        and provide informative feedback to the user.
        """
        try:
            text = self.ids.input_text.text
            if self.state == 0:
                # label text
                self.ids.label.text = 'converted to binary is:'
                # result text
                self.ids.result.text = Converter.dec2bin(text)
            else:
                # label text
                self.ids.label.text = 'converted to decimal is:'
                # result text
                self.ids.result.text = Converter.bin2dec(text)
        except ValueError:
            self.ids.input_text_hint.text = 'Enter a valid number'
            self.ids.result.text = ''
            self.ids.label.text = ''


class BinaryDecimalConverterApp(MDApp):
    """Kivy application class for the binary decimal converter."""

    def build(self):
        self.theme_cls.primary_palette = 'Forestgreen'
        return Converter()


if __name__ == '__main__':
    BinaryDecimalConverterApp().run()
