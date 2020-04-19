'''
 This module provides a simple, and incomplete, abstraction to the GPIO
 library. It is intended for testing and debugging purposes only.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
'''

BOARD       = 0
BCM         = 1
LOW         = 0
HIGH        = 1
IN          = 0
OUT         = 1
DEFAULT_PIN = 17

rotateDeg   = 270
clearFlag   = False
mode        = BCM
curPin      = DEFAULT_PIN
curDir      = IN

def clear():
    clearFlag = True
    
def output(pin = DEFAULT_PIN, direction = IN):
    curPin = pin
    curDir = direction
    
def input(pin = DEFAULT_PIN):
    curPin = pin
    
def set_rotation(rotateDeg):
    rotateDeg = rotateDeg

def setmode(mode = BCM):
    mode = mode
    
def setup(pin = DEFAULT_PIN, direction = IN):
    curPin = pin;
    curDir = direction;
