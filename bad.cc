int main()
{
    const int foo = 0;
    {
        const int foo = 1;
    }
    return foo;
}
