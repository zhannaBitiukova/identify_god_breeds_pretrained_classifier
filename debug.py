

#(images_dir, results_dic, model):

from classifier import classifier 
test_image="pet_images/Beagle_01141.jpg"
path = "pet_images/"
model = "vgg"

filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_label  = classifier(test_image, model).lower().strip()
classifier_labels = []

source_dic = {"Beagle_01141.jpg":["beagle"], "Beagle_01125.jpg":["beagle"], "skunk_029.jpg":["skunk"]}

for i in (source_dic):
    print(i)
    class_label = classifier(path+i, model).lower().strip()
    classifier_labels.append(class_label)


'''
for j in range(len(filenames)):
    class_label = classifier(path+filenames[j], model).lower().strip()
    classifier_labels.append(class_label)
'''
print(classifier_labels)

#results_dic = source_dic.copy()
results_dic = dict()

counter = 0
for j in (source_dic):
    print(j)
    if j not in results_dic:
        results_dic[j] = [source_dic[j][0], classifier_labels[counter]]
        if source_dic[j][0] in classifier_labels[counter]:
            results_dic[j].append(1)
        else:
            results_dic[filenames[i]].append(0)         
    counter += 1
    '''
    if filenames[i] not in results_dic:
        results_dic[filenames[i]] = [pet_labels[i], classifier_labels[i]]
        if pet_labels[i] in classifier_labels[i]:
            results_dic[filenames[i]].append(1)
        else:
            results_dic[filenames[i]].append(0)
    '''

'''
for i in range(len(filenames)):
    if filenames[i] not in results_dic:
        results_dic[filenames[i]] = [pet_labels[i], classifier_labels[i]]
        if pet_labels[i] in classifier_labels[i]:
            results_dic[filenames[i]].append(1)
        else:
            results_dic[filenames[i]].append(0)
''' 



print(results_dic)