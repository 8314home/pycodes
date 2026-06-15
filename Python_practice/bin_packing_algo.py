def bin_pack_first_fit_decreasing(items_with_weights, bin_max_capacity):
    list_of_items = items_with_weights.items()
    # sort by decreasing weights, sorted() create a new list where items will be sorted by weights

    # Why Large Items Are Packed FirstSorting items in decreasing order (largest to smallest) is the defining 
    # step of the First-Fit Decreasing (FFD) algorithm.
    # It provides two major advantages over packing items in a random or increasing order:
    # 1. Avoids Trapping Empty SpaceLarge items are inflexible and difficult to place later.
    # Small items easily fit into the leftover spaces around large items.Packing small items first fills up bins early.
    # Large items left for the end then force the creation of completely new, mostly empty bins.
    
    sorted_list_items = sorted(list_of_items, key= lambda item: item[1], reverse=True)
    print(f'sorted_list_items = {sorted_list_items}')
    bin_collections = []

    # loop item : # take 1 item at a time
    #     loop bin_collections: # take 1 bin at a time from bin_collections
    #         if item weight < bin_capacity - sum(existing item weights of bin):
    #                 append item to bin 
    #                 break 
    #     if no bin found,
    #        create a new bin 
    #        add item to new bin 
    #        append bin to bin_collections
    # Not best solution - but optimal solution - O(N^2)
    for i in sorted_list_items:
        item_weight = i[1] # tuple('item_1',4)
        bin_found = False
        for bin in bin_collections:
            # current_bin capacity
            sum_weights_existing_items_of_bin=0
            for t in bin:
                sum_weights_existing_items_of_bin+= t[1]
            if item_weight < bin_max_capacity - sum_weights_existing_items_of_bin:
                bin.append(i)
                bin_found = True
                break # break from LOOP bin_collections
        #if no bin found 
        if bin_found == False:
            bin_collections.append([i])
    print(f'\n bin_collections = {bin_collections}\n')
    return len(bin_collections)


if __name__ == '__main__':
    items_with_weights = {
        'item_1': 4,
        'item_2': 2,
        'item_3': 7,
        'item_4': 5,
        'item_5': 6,
        'item_6': 3
    }
    BIN_MAX_CAPACITY = 8
    print(f'bin_pack_first_fit_decreasing(items_with_weights, bin_max_capacity) = {bin_pack_first_fit_decreasing(items_with_weights, BIN_MAX_CAPACITY)}')
