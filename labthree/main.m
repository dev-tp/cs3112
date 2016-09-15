#import "LabThree.h"

int main(int argc, char *argv[]) {
    @autoreleasepool {
        NSMutableArray *list = [[NSMutableArray alloc] init];
        [list addObject:[NSNumber numberWithInteger:5]];
        [list addObject:[NSNumber numberWithInteger:1]];
        [list addObject:[NSNumber numberWithInteger:3]];
        [list addObject:[NSNumber numberWithInteger:6]];
        [list addObject:[NSNumber numberWithInteger:21]];
        [list addObject:[NSNumber numberWithInteger:10]];
        [list addObject:[NSNumber numberWithInteger:35]];
        [list addObject:[NSNumber numberWithInteger:44]];
        [list addObject:[NSNumber numberWithInteger:12]];

        NSLog(@"Unsorted NSMutableArray: %@", list.description);

        [LabThree mergeSort:list];
        NSLog(@"Sorted NSMutableArray: %@", list.description);
        
        int result = [LabThree binarySearchList:list toFindElement:[NSNumber numberWithInteger:21]];
        NSLog(@"Found 21 at index: %d", result);

        NSLog(@"5^5 = %.0f", power(5, 5));
        NSLog(@"20^21 = %.0f", power(20, 21));
    }
    return 0;
}