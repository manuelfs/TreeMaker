import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/04DC7D13-1E0C-E511-847C-00A0D1EE923C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/04F32DC9-1E0C-E511-AD5B-848F69FD2955.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/082372A0-290C-E511-ABE2-0025B31E3D3C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/087B1582-A111-E511-8499-002481E1501E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/08AB19D4-1F0D-E511-BCE7-000F530E4784.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/0C5D0549-F90D-E511-9E84-B083FED76520.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/1A073DB8-4B0C-E511-857C-00A0D1EEA584.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/2227ED12-1E0C-E511-BA88-3417EBE6453D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/2278FA80-4C0C-E511-8605-3417EBE338FA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/26260D47-C00D-E511-8C92-002590A80DF4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/267A1E17-1E0C-E511-8E56-00266CF23E68.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/2ADCA7AB-470E-E511-9ED2-00A0D1EC3950.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/360363B6-1E0C-E511-BF66-848F69FD2910.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/38D4F3B6-4B0C-E511-8CFD-008CFA000898.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/3EFA501F-1E0C-E511-9D5E-00266CF25C20.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/409CB818-280C-E511-A90F-0025902009E8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/42F5F412-1E0C-E511-8D68-00266CF25D18.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/44B51FDE-1F0C-E511-BD6B-00A0D1EE8E64.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/463F2B5F-2E0D-E511-8185-047D7BD6DD58.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/4C87DFFD-1F0C-E511-A568-008CFA002020.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/586BA526-E40E-E511-97DA-000F5327375C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/5E6D5392-1F0C-E511-B5FA-00A0D1EE8E64.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/68442360-550C-E511-8C34-842B2B2925F5.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/6CEFDFA6-AA0E-E511-A2A4-001E673975F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/6E700317-1E0C-E511-86E3-00A0D1EEE5CC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/724AAFB7-F20C-E511-9CD2-0025905938AA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/7285772F-1E0C-E511-8B56-00266CF9B8B0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/7A6EF239-520C-E511-9765-782BCB4086A8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/822C1151-240C-E511-A8A3-00A0D1EE8E78.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/88120DF9-430C-E511-A894-047D7B881DD4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/8CD52F84-420C-E511-8FD5-047D7BD6DD44.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/90C2BFDA-310E-E511-AE87-0025904FE658.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/9AAEC95A-5D0D-E511-8861-00266CFAE368.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/9C3D39B7-420C-E511-987A-0025907DCA9C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/9CC83D91-1F0C-E511-92CE-00266CF25D18.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/A6DD00FA-EB0D-E511-8632-0025905964A6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/B41EA471-4C0C-E511-913E-848F69FD4ED4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/C23EDA44-290C-E511-8C6F-002590200894.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/C458B51C-1E0C-E511-B64F-008CFA0021D4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/C62A5F9E-F50C-E511-812C-001E67398223.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/CE8139E6-000D-E511-BCA9-00261894389A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/DC8CEAF7-430C-E511-9DC3-002590DB9188.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/E6678EC3-440C-E511-8C97-0025904B1446.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/F24EDE15-1E0C-E511-B3AE-008CFA0005F4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/1046A02A-040D-E511-A605-9C8E991A143E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/107B586C-1A0E-E511-A776-047D7BD6DE44.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/12BFD30C-EC0C-E511-BA45-7845C4FC35BD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/207603F8-ED0C-E511-8E8E-00A0D1EEA584.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/267EAC51-EC0C-E511-85D8-7845C4FC36E6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/465E41DF-040E-E511-84EB-002590A83192.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/52263406-090D-E511-8646-000F530E4680.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/5A375606-FB0C-E511-BE81-002590A3711C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/6C096EE7-EB0C-E511-94C1-3417EBE644F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/6CA94D08-EC0C-E511-A5FC-7845C4FC37A9.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/701D1F1B-490D-E511-AE21-003048CF632E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/72616EA8-490D-E511-8FC3-0025901D4C3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/782289D2-0A0E-E511-B1B2-3417EBE2F319.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/82816714-EC0C-E511-BB38-848F69FD45E3.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/88B8B847-ED0D-E511-9CB5-B083FED76637.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/926E3B20-EC0C-E511-816C-7845C4FC35BD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/968F6A03-0A0D-E511-8319-000F53273750.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/A0762867-ED0C-E511-AA54-F04DA275987A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/C46F283F-ED0D-E511-B5D4-000F530E4680.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E0CC9D88-ED0C-E511-B245-00266CF9BBE4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E0FE092E-FA0C-E511-B53E-001E67396775.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/ECEEF290-1A0E-E511-90C5-002590DB91BE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F6E8BA83-ED0D-E511-93B4-000F53273730.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/FE163801-090D-E511-A45F-B083FED73FEC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/161AEAEB-7E0C-E511-9181-0025B3E05C60.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/28216580-5A0D-E511-B07E-7845C4FC3B33.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/44982754-810D-E511-A44F-782BCB408696.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/824F9B6E-760D-E511-87DF-0025905A612C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/88D3AB94-650D-E511-A8E1-B083FED73AA1.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/92BD5D64-810D-E511-A269-002590DB9172.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/9E3EEF63-810D-E511-845E-002590AC505C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/A89BBA59-810D-E511-B30D-0025902009B8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/E29D8404-7B0D-E511-87D9-003048FFD728.root' ] );


secFiles.extend( [
               ] )

