import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from scipy import integrate as intg

tree = ET.parse('SPEC0161.N42')
root = tree.getroot()

ns = {
    'xmlns': 'http://physics.nist.gov/Divisions/Div846/Gp4/ANSIN4242/2005/ANSIN4242',
}

# Extract the calibrated channel -> keV mapping
cal = root.find('xmlns:Calibration[@Type="Energy"]', ns)

x, y = [], []
for xy in cal.findall('xmlns:ArrayXY/xmlns:PointXY', ns):
    x.append(int(xy.find('xmlns:X', ns).text.split()[0]))
    y.append(float(xy.find('xmlns:Y', ns).text.split()[0]))

energy = scipy.interpolate.interp1d(x, y)
e = energy(np.arange(512))

# Find the energy units
units = cal.attrib['EnergyUnits']

# Extract the spectrum data
spectrum = root.find('xmlns:Measurement/xmlns:Spectrum/xmlns:ChannelData', ns)
s = np.array(spectrum.text.split(), dtype=np.int16)


#xdata = s[0]
#ydata = s[1]


plt.step(e, s, lw=1, where='post')
plt.ylabel('Counts/bin')
plt.xlabel('Energy (%s)' % units)

plt.xscale('log')
plt.yscale('linear')

#plt.plot([242,242], [0,1700],"red",alpha=0.3)
#plt.text(242, 1050, '$^{226}$Ra',color="red",rotation=90)
#plt.plot([242,242], [0,1700],"green",alpha=0.3)
#plt.text(242, 1800, '$^{226}$Ra',color="green",rotation=90)

#plt.plot([295.4,295.4], [0,1700],"green",alpha=0.3)
#plt.text(295.4, 1800, '$^{214}$Pb',color="green",rotation=90)

#plt.plot([352,352], [0,1700],"green",alpha=0.3)
#plt.text(352, 1800, '$^{214}$Pb',color="green",rotation=90)

#plt.plot([609.3,609.3], [0,1700],"green",alpha=0.3)
#plt.text(609.3, 1800, '$^{214}$Bi',color="green",rotation=90)

#plt.plot([1124.5,1124.5], [0,1700],"green",alpha=0.3)
#plt.text(1124.5, 1800, '$^{214}$Bi',color="green",rotation=90)

#plt.plot([1769,1769], [0,1700],"green",alpha=0.3)
#plt.text(1769, 1800, '$^{214}$Bi',color="green",rotation=90)

#plt.plot([1460,1460], [0,1700],"orange",alpha=0.3)
#plt.text(1460, 1800, '$^{40}$K',color="orange",rotation=90)

#plt.plot([2614,2614], [0,1700],"orange",alpha=0.3)
#plt.text(2614, 1800, '$^{208}$Tl',color="orange",rotation=90)

#plt.plot([384,384], [0,1700],"orange",alpha=0.3)
#plt.text(384, 1800, '$^{239}$Pu',color="orange",rotation=90)


#plt.plot([135,135], [0,1700],"orange",alpha=0.3)
#plt.text(135, 1800, '$^{201}$Tl',color="orange",rotation=90)

#plt.plot([167,167], [0,1700],"orange",alpha=0.3)
#plt.text(167, 1800, '$^{201}$Tl',color="orange",rotation=90)


plt.xlim(100, 4000)
plt.ylim(0, 2000)




#Integral
#y_int = intg.trapz(y, x)
#y_int = intg.simpson(y, x)
#print(y_int)

#print(x , y)
#RangeIntegral = intg.cumtrapz(y, x, initial=2614)
#print(RangeIntegral)





plt.savefig('spectrum.pdf')
plt.show()

