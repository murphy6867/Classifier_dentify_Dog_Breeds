from os import listdir


def get_pet_labels(image_dir):

    in_files = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            # Extracting dog breed name from the filename
            # Assuming that the breed name is the part before the first underscore
            pet_label = in_files[idx].split('_')[0].lower()

            # Strip file extension from the label
            pet_label = pet_label.split('.')[0]

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx].lower()] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:",
                      in_files[idx])

    return results_dic


# Uncomment the lines below for testing
image_dir = './pet_images'
results = get_pet_labels(image_dir)
print(results)
