import type { MouseEvent } from 'react'

/** Stores the pointer position on the element so CSS can draw a soft light under the cursor. */
export function trackPointer(e: MouseEvent<HTMLElement>) {
  const el = e.currentTarget
  const rect = el.getBoundingClientRect()
  el.style.setProperty('--mx', `${e.clientX - rect.left}px`)
  el.style.setProperty('--my', `${e.clientY - rect.top}px`)
}
