from dataModel.accessor import Csvaccessor


sc = Csvaccessor('Gtestdata/oneDimData.csv', 'Gtestdata/DataConfig.json')
testTable = sc.generate()
testTable.create_SegmentT_index("age", "Count", 0.1, 'Gtestdata/Indexresult')
print('finished')




