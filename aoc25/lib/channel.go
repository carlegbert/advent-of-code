package lib

func MapChannel[A any, B any](originalChannel <-chan A, mapper func(A) B) <-chan B {
	ch := make(chan B)
	go func() {
		defer close(ch)
		for val := range originalChannel {
			ch <- mapper(val)
		}
	}()

	return ch
}

func FlatMap[A any, B any](originalChannel <-chan A, mapper func(A) <-chan B) <-chan B {
	ch := make(chan B)
	go func() {
		defer close(ch)
		for val := range originalChannel {
			for b := range mapper(val) {
				ch <- b
			}
		}
	}()

	return ch
}

func ReduceChannel[A any, B any](ch <-chan A, reducer func(B, A) B, accum B) B {
	for val := range ch {
		accum = reducer(accum, val)
	}
	return accum
}
