'''
 This module provides a simple, and incomplete, abstraction to the SenseHAT
 library. It is intended for testing and debugging purposes only.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
'''
from random import uniform

class SenseHat():
    rotateDeg = 270
    clearFlag = False

    def __init__(self):
        self.set_rotation(self.rotateDeg)
    
    def clear(self):
        self.clearFlag = True

    def get_humidity(self):
        # NOTE: This is just a sample
        print('Random humidity value being generated...')
        return round(uniform(30.0, 40.0), 2)
    
    def get_temperature(self):
        return self.get_temperature_from_humidity()
    
    def get_temperature_from_humidity(self):
        # NOTE: This is just a sample
        print('Random temperature value being generated...')
        return round(uniform(18.0, 25.0), 2)
    
    def get_temperature_from_pressure(self):
        return self.get_temperature_from_humidity()
    
    def get_pressure(self):
        # NOTE: This is just a sample
        print('Random pressure value being generated...')
        return round(uniform(1020.0, 1035.0), 2)
            
    def set_rotation(self, rotateDeg):
        self.rotateDeg = rotateDeg
    
    def show_letter(self, val):
        print(val)
    
    def show_message(self, msg):
        print(msg)
