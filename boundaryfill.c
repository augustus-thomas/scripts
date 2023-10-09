struct point
{
	int x;
	int y;
};

struct pixel
{
	struct point position;
	int color;
};

struct line
{
	struct point start;
	struct point end;
};

class image
{
	struct framebuffer; //array of pixels mxn
	struct polygons; //set of lines
}

void boundaryfill4(int x, int y, int b, int f)
{
	int current=getPixel(x,y);
	if ((current != b) && (current!=f)
	{
		setColor(f);
		setPixel(x,y);
		boundaryfill4(x, y+1, b, f);
		boundaryfill4(x+1, y, b, f);
		boundaryfill4(x-1, y, b, f);
		boundaryfill4(x, y-1, b, f);
	}
}
