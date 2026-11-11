import type { ReactNode } from 'react'

type Tone = 'emerald' | 'amber' | 'indigo' | 'neutral'

const tones: Record<Tone, string> = {
  emerald: 'bg-primary/12 text-primary-light border-primary/25',
  amber: 'bg-caution/12 text-caution-light border-caution/25',
  indigo: 'bg-govern/12 text-govern-soft border-govern/25',
  neutral: 'bg-white/5 text-ink-soft border-white/10',
}

/** Pill badge in mono type with a status dot (Institutional status chips). */
export function StatusChip({
  tone = 'neutral',
  live = false,
  children,
  className = '',
}: {
  tone?: Tone
  live?: boolean
  children: ReactNode
  className?: string
}) {
  return (
    <span
      className={`num inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-[10px] font-medium uppercase tracking-wider ${tones[tone]} ${className}`}
    >
      <span className={`dot ${live ? 'dot-live' : ''}`} aria-hidden />
      {children}
    </span>
  )
}
