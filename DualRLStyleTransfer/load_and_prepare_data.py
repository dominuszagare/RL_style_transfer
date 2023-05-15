def load_dataset_yelp_reviews():
    rewiev_files = ["./DualRLStyleTransfer/yelp_data/test.0",
                "./DualRLStyleTransfer/yelp_data/test.1",
                "./DualRLStyleTransfer/yelp_data/dev.0",
                "./DualRLStyleTransfer/yelp_data/dev.1",
                "./DualRLStyleTransfer/yelp_data/train.0",
                "./DualRLStyleTransfer/yelp_data/train.1",
                "./DualRLStyleTransfer/yelp_refrence/reference0.0",
                  "./DualRLStyleTransfer/yelp_refrence/reference0.1",
                  "./DualRLStyleTransfer/yelp_refrence/reference1.0",
                  "./DualRLStyleTransfer/yelp_refrence/reference1.1",
                    "./DualRLStyleTransfer/yelp_refrence/reference2.0",
                    "./DualRLStyleTransfer/yelp_refrence/reference2.1",
                  "./DualRLStyleTransfer/yelp_refrence/reference3.0",
                  "./DualRLStyleTransfer/yelp_refrence/reference3.1"]

    train_data = []
    test_data = []
    dev_data = []
    references_to_test = []

    for i in range(0, len(rewiev_files)):
        print(rewiev_files[i])
        with open(rewiev_files[i]) as f:
            lines = f.readlines()
            #remove \n from end of line
            lines = [x.strip() for x in lines]
            lines = [x.replace(" .",".") for x in lines]
            lines = [x.replace(" !","!") for x in lines]
            lines = [x.replace(" ?","?") for x in lines]
            lines = [x.replace(" '","'") for x in lines]
            lines = [x.replace(' ,',',') for x in lines]
            lines = [x.replace(' )',')') for x in lines]
            lines = [x.replace(' :',':') for x in lines]
            lines = [x.replace('( ','(') for x in lines]
            lines = [x.replace(' - ','-') for x in lines]
            lines = [x.replace('$ _num_','$_num_') for x in lines]
            lines = [x.replace('_num_ $','_num_$') for x in lines]
            #create sentiment list same size as lines
            if i % 2 == 0:
                sen = 'NEGATIVE'
            else:
                sen = 'POSITIVE'
            sentiment = [sen] * len(lines)
            #add lines and sentiment to train_data_XY array
            data = []
            for j in range(0,len(lines)):
                data.append({'input':lines[j], 'label':sentiment[j]})
            if i > 5:
                references_to_test.extend(data)
            elif i > 3:
                train_data.extend(data)
            elif i > 1:
                dev_data.extend(data)
            else:
                test_data.extend(data)
                
    test_data_and_references = []
    len_test_data = len(test_data)
    ref_number = int(len(references_to_test)/len_test_data)
    for i in range(0, len_test_data):
        ref = []
        for n in range(0, ref_number):
            ref.append(references_to_test[i+n*len_test_data]['input'])
        test_data_and_references.append({'input':test_data[i]['input'], 'label':test_data[i]['label'], 'ref':ref})

    return train_data, test_data, dev_data, test_data_and_references