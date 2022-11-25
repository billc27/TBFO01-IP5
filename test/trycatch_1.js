try {
    if (x == 2) throw 3;
} catch (err) {
    x++;
} finally {
    a++;
}