#import "LabThree.h"

double power(double a, int n) {
    if (n == 0)
        return 1;
    
    double t = power(a, n / 2);
    
    if (n % 2 == 0)
        return t * t;
    else
        if (n > 0)
            return a * t * t;
        else
            return (t * t) / a;
}

@implementation LabThree

+ (void)mergeSort:(NSMutableArray *)list {
    NSMutableArray *sideList = [NSMutableArray arrayWithArray:list];

    for (int i = 1; i < list.count; i *= 2) {
        for (int j = 0; j < list.count; j += i * 2)
            [LabThree mergeSortWithList:list
                              leftIndex:j
                             rightIndex:min(i + j, (int) list.count)
                                    tip:min(j + 2 * i, (int) list.count)
                               sideList:sideList];
        [list setArray:sideList];
    }
}

+ (void)mergeSortWithList:(NSMutableArray *)list
                leftIndex:(int)leftIndex
               rightIndex:(int)rightIndex
                      tip:(int)tip
                 sideList:(NSMutableArray *)sideList {

    int i = leftIndex, j = rightIndex;

    for (int k = leftIndex; k < tip; k++)
        if (i < rightIndex && (j >= tip || list[i] <= list[j]))
            sideList[k] = list[i++];
        else
            sideList[k] = list[j++];
}

+ (int)binarySearchList:(NSMutableArray *)list toFindElement:(id)element {
    int lowestIndex = 0, highestIndex = (int) list.count - 1;

    while (lowestIndex <= highestIndex) {
        int indexInBetween = lowestIndex + (highestIndex - lowestIndex) / 2;
        if (element < list[indexInBetween])
            highestIndex = indexInBetween - 1;
        else if (element > list[indexInBetween])
            lowestIndex = indexInBetween + 1;
        else
            return indexInBetween;
    }

    return -1;
}

@end