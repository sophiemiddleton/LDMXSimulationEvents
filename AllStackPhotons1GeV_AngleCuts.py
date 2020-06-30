from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TLorentzVector, TF1
import math
data0=[]
data1=[]
data2=[]
data3=[]
data4 =[]
EventWeight = 0.3678
Lumi = 0.22
ProtonsPerN = 74
Factor5 = 6.063*Lumi*ProtonsPerN
Factor30 = 0.1795*Lumi*ProtonsPerN
Factor20 = 0.4495*Lumi*ProtonsPerN
Factor10 = 1.851*Lumi*ProtonsPerN
Factor15 = 0.8324*Lumi*ProtonsPerN
Factor25 = 0.2666*Lumi*ProtonsPerN
FF=3
if FF==1:
    Eventweight =278.4
    data1=readLHEF('FFop1_cuts/30deg.lhe')
if FF == 2:
    Eventweight= 0.0002478
    data1=readLHEF('FFop2_cuts/30deg.lhe')
if FF==3:
    Eventweight = 0.3678
    data0=readLHEF('FFop3_cuts/5deg_1.lhe')
    data1=readLHEF('FFop3_cuts/30_1.lhe')
    data2=readLHEF('FFop3_cuts/20deg_1.lhe')
    data3=readLHEF('FFop3_cuts/10deg_1.lhe')
    data4=readLHEF('FFop3_cuts/15deg_1.lhe')
    data5=readLHEF('FFop3_cuts/25deg_1.lhe')
if FF==4:
    Eventweight = 0.003193
    data1=readLHEF('FFop4_cuts/30deg.lhe')

print("FF is :",FF," Event Weight is : ", EventWeight)
electrons0=data0.getParticlesByIDs([22,-22])
electrons1=data1.getParticlesByIDs([22,-22])
electrons2=data2.getParticlesByIDs([22,-22])
electrons3=data3.getParticlesByIDs([22,-22])
electrons4=data4.getParticlesByIDs([22,-22])
electrons5=data5.getParticlesByIDs([22,-22])
c=TCanvas()
c.Divide(2,2)
c_mom=TCanvas()
c_mom.Divide(2,2)
clab=TCanvas()
clab.Divide(2,2)

hist_e_theta_out=TH1F("theta_elec_out", "Outgoing Electron Theta",100,0, math.pi)
hist_e_phi_out=TH1F("phi_elec_out", "Outgoing Electron Phi",100,-math.pi,math.pi)
hist_4in=TH1F("q^{2} in", "Incoming Electron q^{2} ", 100,0,0.00001)
hist_4out=TH1F("q^{2} out", "Outgoing Electron q^{2} ", 100,0,0.00001)

hist_Px_out_5Deg=TH1F("P_{z} out 5 deg", "#theta_{min}=5 ", 100,-5,5)
hist_Pz_out_5Deg=TH1F("P_{x} out 5 deg", "#theta_{min}=5", 100,-5,5)
hist_Py_out_5Deg=TH1F("P_{y} out 5 deg", "#theta_{min}=5 ", 100,-5,5)
hist_E_out_5Deg=TH1F("E out 5 deg", "#theta_{min}=5", 100,0,5)

hist_Px_out_10Deg=TH1F("P_{z} out 10 deg", "#theta_{min}=10 ", 100,-5,5)
hist_Pz_out_10Deg=TH1F("P_{x} out 10 deg", "#theta_{min}=10", 100,-5,5)
hist_Py_out_10Deg=TH1F("P_{y} out 10 deg", "#theta_{min}=10 ", 100,-5,5)
hist_E_out_10Deg=TH1F("E out 10 deg", "#theta_{min}=10", 100,0,5)

hist_Px_out_15Deg=TH1F("P_{z} out 15 deg", "#theta_{min}=15 ", 100,-5,5)
hist_Pz_out_15Deg=TH1F("P_{x} out 15 deg", "#theta_{min}=15", 100,-5,5)
hist_Py_out_15Deg=TH1F("P_{y} out 15 deg", "#theta_{min}=15 ", 100,-5,5)
hist_E_out_15Deg=TH1F("E out 15 deg", "#theta_{min}=15", 100,0,5)

hist_Px_out_20Deg=TH1F("P_{z} out 20 deg", "#theta_{min}=20", 100,-5,5)
hist_Pz_out_20Deg=TH1F("P_{x} out 20 deg", "#theta_{min}=20", 100,-5,5)
hist_Py_out_20Deg=TH1F("P_{y} out 20 deg", "#theta_{min}=20", 100,-5,5)
hist_E_out_20Deg=TH1F("E out  20 deg", "#theta_{min}=20", 100,0,5)

hist_Px_out_25Deg=TH1F("P_{z} out 25 deg", "#theta_{min}=25 ", 100,-5,5)
hist_Pz_out_25Deg=TH1F("P_{x} out 25 deg", "#theta_{min}=25", 100,-5,5)
hist_Py_out_25Deg=TH1F("P_{y} out 25 deg", "#theta_{min}=25 ", 100,-5,5)
hist_E_out_25Deg=TH1F("E out 25 deg", "#theta_{min}=25", 100,0,5)

hist_Px_out_30Deg=TH1F("P_{z} out 30 deg", "#theta_{min}=30", 100,-5,5)
hist_Pz_out_30Deg=TH1F("P_{x} out 30 deg", "#theta_{min}=30", 100,-5,5)
hist_Py_out_30Deg=TH1F("P_{y} out 30 deg", "#theta_{min}=30", 100,-5,5)
hist_E_out_30Deg=TH1F("E out 30 deg", "#theta_{min}=30", 100,0,5)

for e in electrons0:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor5))
        hist_e_theta_out.Fill(theta,(Factor5))
        hist_4out.Fill(squared_4mom,(Factor5))
        hist_Px_out_5Deg.Fill(e.px,(Factor5))
        hist_Py_out_5Deg.Fill(e.py,(Factor5))
        hist_Pz_out_5Deg.Fill(e.pz,(Factor5))
        hist_E_out_5Deg.Fill(e.energy,(Factor5))

for e in electrons1:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor30))
        hist_e_theta_out.Fill(theta,(Factor30))
        hist_4out.Fill(squared_4mom,(Factor30))
        hist_Px_out_30Deg.Fill(e.px,(Factor30))
        hist_Py_out_30Deg.Fill(e.py,(Factor30))
        hist_Pz_out_30Deg.Fill(e.pz,(Factor30))
        hist_E_out_30Deg.Fill(e.energy,(Factor30))

for e in electrons2:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor20))
        hist_e_theta_out.Fill(theta,(Factor20))
        hist_4out.Fill(squared_4mom,(Factor20))
        hist_Px_out_20Deg.Fill(e.px,(Factor20))
        hist_Py_out_20Deg.Fill(e.py,(Factor20))
        hist_Pz_out_20Deg.Fill(e.pz,(Factor20))
        hist_E_out_20Deg.Fill(e.energy,(Factor20))

for e in electrons3:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor10))
        hist_e_theta_out.Fill(theta,(Factor10))
        hist_4out.Fill(squared_4mom,(Factor10))
        hist_Px_out_10Deg.Fill(e.px,(Factor10))
        hist_Py_out_10Deg.Fill(e.py,(Factor10))
        hist_Pz_out_10Deg.Fill(e.pz,(Factor10))
        hist_E_out_10Deg.Fill(e.energy,(Factor10))
for e in electrons4:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor15))
        hist_e_theta_out.Fill(theta,(Factor15))
        hist_4out.Fill(squared_4mom,(Factor15))
        hist_Px_out_15Deg.Fill(e.px,(Factor15))
        hist_Py_out_15Deg.Fill(e.py,(Factor15))
        hist_Pz_out_15Deg.Fill(e.pz,(Factor15))
        hist_E_out_15Deg.Fill(e.energy,(Factor15))
for e in electrons5:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor25))
        hist_e_theta_out.Fill(theta,(Factor25))
        hist_4out.Fill(squared_4mom,(Factor25))
        hist_Px_out_25Deg.Fill(e.px,(Factor25))
        hist_Py_out_25Deg.Fill(e.py,(Factor25))
        hist_Pz_out_25Deg.Fill(e.pz,(Factor25))
        hist_E_out_25Deg.Fill(e.energy,(Factor25))
c.cd(1)
hist_e_theta_out.GetXaxis().SetTitle("#theta[rad]")
hist_e_theta_out.Draw()
c.cd(2)
hist_e_phi_out.GetXaxis().SetTitle("#phi[rad]")
hist_e_phi_out.Draw()
c.cd(3)
hist_4in.GetXaxis().SetTitle("q^{2}_{e_{in}}")
hist_4in.Draw()
c.cd(4)
hist_4out.GetXaxis().SetTitle("q^{2}_{e_{out}}")
hist_4out.Draw()
c.SaveAs("electron_angle_plots_lab_30deg"+str(FF)+".root")

c_mom.cd(1)
hist_Px_out_5Deg.GetXaxis().SetTitle("P_{x}")
hist_Px_out_5Deg.Draw('HIST')
hist_Px_out_10Deg.SetLineColor(3)
hist_Px_out_10Deg.Draw('HISTSAME')
hist_Px_out_15Deg.SetLineColor(2)
hist_Px_out_15Deg.Draw('HISTSAME')
hist_Px_out_20Deg.SetLineColor(7)
hist_Px_out_20Deg.Draw('HISTSAME')
hist_Px_out_25Deg.SetLineColor(28)
hist_Px_out_25Deg.Draw('HISTSAME')
hist_Px_out_30Deg.SetLineColor(6)
hist_Px_out_30Deg.Draw('HISTSAME')
c_mom.cd(2)
hist_Py_out_5Deg.GetXaxis().SetTitle("P_{y}")
hist_Py_out_5Deg.Draw('HIST')
hist_Py_out_10Deg.SetLineColor(3)
hist_Py_out_10Deg.Draw('HISTSAME')
hist_Py_out_15Deg.SetLineColor(2)
hist_Py_out_15Deg.Draw('HISTSAME')
hist_Py_out_20Deg.SetLineColor(7)
hist_Py_out_20Deg.Draw('HISTSAME')
hist_Py_out_25Deg.SetLineColor(28)
hist_Py_out_25Deg.Draw('HISTSAME')
hist_Py_out_30Deg.SetLineColor(6)
hist_Py_out_30Deg.Draw('HISTSAME')
c_mom.cd(3)
hist_Pz_out_5Deg.GetXaxis().SetTitle("P_{z}")
hist_Pz_out_5Deg.Draw('HIST')
hist_Pz_out_10Deg.SetLineColor(3)
hist_Pz_out_10Deg.Draw('HISTSAME')
hist_Pz_out_15Deg.SetLineColor(2)
hist_Pz_out_15Deg.Draw('HISTSAME')
hist_Pz_out_20Deg.SetLineColor(7)
hist_Pz_out_20Deg.Draw('HISTSAME')
hist_Pz_out_25Deg.SetLineColor(28)
hist_Pz_out_25Deg.Draw('HISTSAME')
hist_Pz_out_30Deg.SetLineColor(6)
hist_Pz_out_30Deg.Draw('HISTSAME')
c_mom.cd(4)
hist_E_out_5Deg.GetXaxis().SetTitle("E")
hist_E_out_5Deg.Draw('HIST')
hist_E_out_10Deg.SetLineColor(3)
hist_E_out_10Deg.Draw('HISTSAME')
hist_E_out_15Deg.SetLineColor(2)
hist_E_out_15Deg.Draw('HISTSAME')
hist_E_out_20Deg.SetLineColor(7)
hist_E_out_20Deg.Draw('HISTSAME')
hist_E_out_25Deg.SetLineColor(28)
hist_E_out_25Deg.Draw('HISTSAME')
hist_E_out_30Deg.SetLineColor(6)
hist_E_out_30Deg.Draw('HISTSAME')
c_mom.SaveAs("photon_mom_plots_lab_30deg"+str(FF)+".root")
