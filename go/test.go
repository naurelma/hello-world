package main

import "kuva"

func Pic(dx, dy int) [][]uint8 {
	a := make([][]uint8, dy)
	for i := 0; i < dy; i++ {
		a[i] = make([]uint8, dx)
	}
	for i := 0; i < dy; i++ {
		for j := 0; j < dx; j++ {
			a[i][j] = uint8(i*j)
		}
	}

	return a
}

func main() {
	kuva.Show(Pic)
}
