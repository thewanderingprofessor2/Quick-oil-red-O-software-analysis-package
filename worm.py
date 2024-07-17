import sys
import importlib

# Function to check if a package is installed
def check_package_installed(package_name, module_name=None):
    if module_name is None:
        module_name = package_name
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

# Check for numpy and PIL (Pillow)
if not check_package_installed('numpy'):
    print("Please type 'pip install numpy' into the terminal.")

if not check_package_installed('Pillow', 'PIL'):
    print("Please type 'pip install Pillow' into the terminal.")

# Exit if necessary packages aren't installed
if not (check_package_installed('numpy') and check_package_installed('Pillow', 'PIL')):
    sys.exit()

# Rest of your original code starts here
import glob
from PIL import Image
import numpy

print('imports')

path_to_images = "/Users/lcato/worm/images/*.tif"
path_to_report = "/Users/lcato/worm/reports/report.txt"

filenames = glob.glob(path_to_images)
print(filenames)

def picstat(filenames, report):
    n = 1
    for file in filenames:
        report.write(file[0:-4])
        report.write('\t')

        print('converting ', file, ' to grayscale')
        im = Image.open(file).convert("I")
        data = im.getdata()
        data = list(data)

        def reverse(x):
            return 255 - x

        data = list(map(reverse, data))

        total = numpy.sum(data)
        mean = numpy.mean(data)
        stdev = numpy.std(data)

        print(file, ' converted!. found ', total, ' pixels with a mean brightness of ', mean, ' and a std. deviation of ', stdev)

        def cropper(x):
            return x if x > mean + stdev * 1.5 else 0

        fg_data = list(map(cropper, data))

        pic = Image.new('I', (2048, 1536))
        pic.putdata(fg_data)

        if n < 10:
            file_list = list(file)
            newfile = []
            file_list.append('_1.5afiltered.tiff')
            newfile = ''.join(file_list)
            pic.save(newfile, 'TIFF')
            n += 1

        fg_total = numpy.sum(fg_data)

        def calarea(data):
            area = 0
            for x in data:
                if x > 0:
                    area += 1
            return area

        area = calarea(fg_data)

        bg_total = total - fg_total
        bg_mean = bg_total / ((2048.0 * 1536.0) - area)

        fg_net_total = fg_total - bg_mean * area
        fg_net_mean = fg_net_total / area

        print('writing the following report to file: ', report, '\n')
        print('\t', 'file Name', '\t\t\t', 'worm total  ', '\t', 'worm area', '\t', 'worm mean pixel brightness')
        print(filenames, '\t', fg_net_total, '\t', area, '\t\t', fg_net_mean, '\n')

        report.write(str(fg_net_total))
        report.write('\t')
        report.write(str(area))
        report.write('\t')
        report.write(str(fg_net_mean))
        report.write('\n')


with open(path_to_report, 'at') as report:
    picstat(filenames, report)
    report.write('\n\n')
