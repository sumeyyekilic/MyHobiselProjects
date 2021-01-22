#  *********************************************************
#  **     @sumklc                                         **
#  **     Sümeyye kılıç                                   **
#  **     10.01.2021                                      **
#  **     Hobisel -unutulan python bilgilerini tazeleme   **
#  **     -SublimeText                                    **
#  *********************************************************

#!/usr/bin/python
# -*- coding: utf-8 -*- 

class Developerella:
    """bir developer'Ella kolay yetişmiyor.."""
    """worker-- deneme-1-2"""

    def __init__(self, name, lastname, job):

        self.name  = name
        self.lastname = lastname
        self.job= job

        print('Created Developerella: {} - {}'.format(self.fullName, self.jobTl))
        print('For Projects -------> {} <-------'.format(self.githubAddress))

    @property
    def githubAddress(self):
        return 'https://github.com/{}{}'.format(TrEnTrans(self.name), TrEnTrans(self.lastname)).lower()

    @property
    def fullName(self):
        return '{} {}'.format(self.name, self.lastname).upper()

    @property
    def jobTl(self):
        return '{}'.format(self.job).title()


def TrEnTrans(gonderSUM):
    str      = gonderSUM

    translate   = ''
    charsTR = [('ı','i'),('ü','u'),('ö','o'),('ç','c'),('ğ','g'),('ş','s')]

    for translate, chars in charsTR:
        str  = str.replace(translate, chars)
    return str


if __name__ == '__main__':

    print(Developerella('sümeyye','kılıç','web developer"Ella  :)'))
