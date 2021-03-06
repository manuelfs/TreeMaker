import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/0C0AED81-735C-E511-9E10-003048947D6C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/1A000693-725C-E511-A820-002590D9D8BA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/1E60F193-725C-E511-AF7E-20CF3027A62B.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/2C9E3897-725C-E511-B5E4-B083FED13803.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/2E637C9B-725C-E511-BC10-C8600032C755.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/3AB48995-725C-E511-9A53-0025907277FE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/3EA33493-725C-E511-9F96-44A84225CDA4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/42AFEA9A-725C-E511-AC03-B083FECFD4F0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/44C7AAF1-735C-E511-9215-002590FD5A52.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/4AEDC40A-745C-E511-9365-002590D9D8AA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/548E5F15-745C-E511-A480-002590D9D8B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5E85D293-725C-E511-89C5-001E675A6A63.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/62E4E095-725C-E511-8596-44A84225D36F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/70281899-725C-E511-9B93-B083FED04276.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/70959991-725C-E511-A6CC-0025901AC3C6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/84571A95-725C-E511-91C9-002590FD5A72.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/8EF16E97-725C-E511-92FE-00259073E512.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/923B7E99-725C-E511-96E7-00259073E52A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/947681CF-745C-E511-AB44-0CC47A0AD3BC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/96547358-745C-E511-9731-0CC47A0AD3BC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9AB26A92-725C-E511-8BC7-001E675A69DC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9CB7FEA6-725C-E511-92BD-002590D8C68A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9E212C9A-725C-E511-9F0D-B083FED13803.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A04A03D8-FE5D-E511-BF99-90B11C070100.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A0DCE794-725C-E511-92B3-002590FD5A52.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A2D5F8A1-725C-E511-8B2F-0CC47A0AD6E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A81C1A98-725C-E511-8E41-002590D9D8B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/AA007A14-745C-E511-8F95-0CC47A0AD6E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/B080DA9D-725C-E511-8349-D4856459AC30.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/BA515999-725C-E511-A308-002590D9D8AA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/BC619BA4-725C-E511-B7F3-002590207C28.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/C4B0F4F2-735C-E511-BC72-002590D9D8BA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/D4A8C4D9-735C-E511-87BD-002590FD5A72.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E21C7CA6-725C-E511-BDD9-002590D60042.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E407149A-725C-E511-A757-B083FED16468.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E4AB898F-725C-E511-94E3-003048947A8E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/EE3F7CA4-725C-E511-84AC-F4CE46B27A1A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/F2E95298-725C-E511-8027-002590D4FC5C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/142B774C-2D5C-E511-B03C-20CF3027A607.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/1C6255DE-325C-E511-B433-002590D9D96E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/321DA069-2C5C-E511-ABFB-001E67A4069F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/42BC492B-305C-E511-B2E2-003048947CC6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/6C3DE84D-2D5C-E511-919E-20CF3027A561.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/8EA7E58D-315C-E511-BAB1-002590D9D96E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/9C695755-2D5C-E511-8719-003048947CC6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/A625B9A0-325C-E511-8F4D-002590D9D8BC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D81A891E-315C-E511-96A5-002590D9D8BC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/FCFF1F55-2D5C-E511-8A6F-A4BADB3D00FF.root' ] );


secFiles.extend( [
               ] )

