export const includesAll = (a: any[], b: Set<any>): boolean => {
    for (const entry of b) {
        if(!a.includes(entry)) return false;
    }
    return true;
}