from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TLorentzVector, TF1
import math

Lumi = 0.22
ProtonsPerN = 74
FactorFF1 = 281.1*Lumi*ProtonsPerN
FactorFF2 = 0.0002394*Lumi*ProtonsPerN
FactorFF3 =  0.1795*Lumi*ProtonsPerN
FactorFF4 = 0.001583*Lumi*ProtonsPerN
data01 =readLHEF('FFop1_cuts/30deg_1.lhe')
data02 =readLHEF('FFop2_cuts/30deg_1.lhe')
data03 =readLHEF('FFop3_cuts/30_1.lhe')
data04 =readLHEF('FFop4_cuts/30deg_1.lhe')

electrons01=data01.getParticlesByIDs([9000002,-9000002])
electrons02=data02.getParticlesByIDs([9000002,-9000002])
electrons03=data03.getParticlesByIDs([9000002,-9000002])
electrons04=data04.getParticlesByIDs([9000002,-9000002])

c=TCanvas()
c.Divide(2,2)
c1=TCanvas()
c1.Divide(2,2)
hist_4mom_diff_opt1=TH1F("#Delta q^{2} in opt1", "Outgoing - Incoming Nucleus q^{2} opt1", 100,-50,20)
hist_4mom_diff_opt2=TH1F("#Delta q^{2} in opt2", "Outgoing - Incoming Nucelus q^{2} opt2", 100,-50,20)
hist_4mom_diff_opt3=TH1F("#Delta q^{2} in opt3", "Outgoing - Incoming Nucelus q^{2} opt3", 100,-6,0)
hist_4mom_diff_opt4=TH1F("#Delta q^{2} in opt4", "Outgoing - Incoming Nucelus q^{2} opt4", 100,-6,0)
hist_4momRatio12=TH1F("q^{2} out opt1/opt2", "Ratio q^{2} of opt1/opt2 ", 100,-50,20)
hist_4momRatio34=TH1F("q^{2} out opt3/opt4", "Ratio q^{2} of opt3/opt4 ", 100,-6,0)
incoming_values_p_opt1 = []
outgoing_values_p_opt1 = []
incoming_values_p_opt2 = []
outgoing_values_p_opt2 = []
outgoing_values_p_opt3 = []
incoming_values_p_opt3 = []
outgoing_values_p_opt4 = []
incoming_values_p_opt4 = []
func  = TF1( 'fun1', '(1/[(1+x/0.0050695)^2])',-0.4,0 )
for i, e in enumerate(electrons01):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt1.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt1.append(outgoing)

for j, event in enumerate(incoming_values_p_opt1):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt1[j] - incoming_values_p_opt1[j]
    hist_4mom_diff_opt1.Fill(qdiff.M2(),FactorFF1)

for i, e in enumerate(electrons02):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt2.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt2.append(outgoing)

for j, event in enumerate(incoming_values_p_opt2):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt2[j] - incoming_values_p_opt2[j]
    hist_4mom_diff_opt2.Fill(qdiff.M2(),FactorFF2)

for i, e in enumerate(electrons03):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt3.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt3.append(outgoing)

for j, event in enumerate(incoming_values_p_opt3):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt3[j] - incoming_values_p_opt3[j]
    hist_4mom_diff_opt3.Fill(qdiff.M2(),FactorFF3)
    print(qdiff.M2())

for i, e in enumerate(electrons04):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt4.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt4.append(outgoing)

for j, event in enumerate(incoming_values_p_opt4):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt4[j] - incoming_values_p_opt4[j]
    hist_4mom_diff_opt4.Fill(qdiff.M2(),FactorFF4)

c.cd(1)
hist_4mom_diff_opt1.GetXaxis().SetTitle("#Delta q^{2} [GeV/c]")
hist_4mom_diff_opt1.Draw("HIST")
c.cd(2)
hist_4mom_diff_opt2.GetXaxis().SetTitle("#Delta q^{2} [GeV/c]")
hist_4mom_diff_opt2.Draw("HIST")
for i in range(0,hist_4mom_diff_opt2.GetNbinsX()):
    if hist_4mom_diff_opt2.GetBinContent(i) !=0 :
        ratio12 = hist_4mom_diff_opt1.GetBinContent(i)/hist_4mom_diff_opt2.GetBinContent(i)
        hist_4momRatio12.SetBinContent(i,ratio12)
c.cd(3)
hist_4momRatio12.Draw()
c.SaveAs("compare4mom_op12_withcuts.root")
c1.cd(1)
hist_4mom_diff_opt3.GetXaxis().SetTitle("#Delta q^{2} [GeV/c]")
hist_4mom_diff_opt3.Draw("HIST")
c1.cd(2)
hist_4mom_diff_opt4.GetXaxis().SetTitle("#Delta q^{2} [GeV/c]")
hist_4mom_diff_opt4.Draw("HIST")
for i in range(0,hist_4mom_diff_opt4.GetNbinsX()):
    if hist_4mom_diff_opt4.GetBinContent(i) !=0 :
        ratio34 = hist_4mom_diff_opt3.GetBinContent(i)/hist_4mom_diff_opt4.GetBinContent(i)
        hist_4momRatio34.SetBinContent(i,ratio34)
c1.cd(3)
hist_4momRatio34.Draw()
c1.SaveAs("compare4mom_op34_withcut.root")
