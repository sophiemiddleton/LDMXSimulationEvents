from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data=readLHEF('unweighted_events.lhe')
electrons=data.getParticlesByIDs([11,-11])
c=TCanvas()
c.Divide(2,2)
hist_e_theta=TH1F("theta_elec", "Electron Theta",100,-1,1)
hist_4mom=TH2F("4mom ratio", "4mom in v 4mom out", 100,0,100,100,0,100)

for e in electrons:
    val = math.atan(e.py/e.pz)
    hist_e_theta.Fill(val)
    squared_out = 1;
    squared_in = 1;
    hist_4mom.Fill(squared_out, squared_in)
c.cd(1)
hist_e_theta.GetXaxis().SetTitle("#theta")
hist_e_theta.Draw()
c.SaveAs("electron_plots.png")
