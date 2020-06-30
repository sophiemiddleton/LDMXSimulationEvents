from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data02 =readLHEF('run02/unweighted_events.lhe')
data03 =readLHEF('run03/unweighted_events.lhe')
electrons02=data02.getParticlesByIDs([11,-11])
electrons03=data03.getParticlesByIDs([11,-11])

c=TCanvas()
c.Divide(2,2)
hist_e_theta02=TH1F("theta_elec v02", "Outgoing Electron Theta",100,-1,1)
hist_e_theta03=TH1F("theta_elec v03", "Outgoing Electron Theta",100,-1,1)
for e in electrons02:
    if e.status is 1:
        val = math.atan(e.py/e.pz)
        hist_e_theta02.Fill(val)

for e in electrons03:
    if e.status is 1:
        val = math.atan(e.py/e.pz)
        hist_e_theta03.Fill(val)

c.cd(1)
hist_e_theta02.GetXaxis().SetTitle("#theta")
hist_e_theta02.Draw()
hist_e_theta03.GetXaxis().SetTitle("#theta")
hist_e_theta03.Draw("same")
c.SaveAs("compare.png")
