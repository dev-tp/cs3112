#import <Foundation/Foundation.h>

#define min(a, b) (a < b ? a : b)

double power(double base, long exponent);

@interface LabThree : NSObject

+ (void)mergeSort:(NSMutableArray *)list;
+ (int)binarySearchList:(NSMutableArray *)list toFindElement:(id)element;

@end