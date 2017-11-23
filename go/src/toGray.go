package main

import (
    "image"
    _ "image/jpeg" // Register JPEG format
    "image/png"    // Register PNG  format
    "image/color"
    "log"
    "os"
)

// Converted implements image.Image, so you can
// pretend that it is the converted image.
type Converted struct {
    Img image.Image
    Mod color.Model
}

// We return the new color model...
func (c *Converted) ColorModel() color.Model{
    return c.Mod
}

// ... but the original bounds
func (c *Converted) Bounds() image.Rectangle{
    return c.Img.Bounds()
}

// At forwards the call to the original image and
// then asks the color model to convert it.
func (c *Converted) At(x, y int) color.Color{
    return c.Mod.Convert(c.Img.At(x,y))
}

func main() {
    if len(os.Args) != 3 { log.Fatalln("Needs two arguments")}
    infile, err := os.Open(os.Args[1])
    if err != nil {
        log.Fatalln(err)
    }
    defer infile.Close()

    img, _, err := image.Decode(infile)
    if err != nil {
        log.Fatalln(err)
    }

    // Since Converted implements image, this is now a grayscale image
    gr := &Converted{img, color.GrayModel}
    // Or do something like this to convert it into a black and
    // white image.
    // bw := []color.Color{color.Black,color.White}
    // gr := &Converted{img, color.Palette(bw)}


    outfile, err := os.Create(os.Args[2])
    if err != nil {
        log.Fatalln(err)
    }
    defer outfile.Close()

    png.Encode(outfile,gr)
}