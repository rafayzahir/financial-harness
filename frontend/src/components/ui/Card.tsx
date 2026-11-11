import type { CSSProperties, ReactNode } from 'react'
import { trackPointer } from '../../lib/pointer'

interface CardProps {
  title?: string
  subtitle?: string
  action?: ReactNode
  children: ReactNode
  className?: string
  /** Entrance delay in ms, used to stagger cards */
  delay?: number
}

export function Card({ title, subtitle, action, children, className = '', delay = 0 }: CardProps) {
  return (
    <section
      onMouseMove={trackPointer}
      style={{ '--d': `${delay}ms` } as CSSProperties}
      className={`surface spotlight lift enter p-6 ${className}`}
    >
      {(title || action) && (
        <header className="mb-5 flex items-start justify-between gap-3">
          <div>
            {title && <h2 className="font-display text-lg font-medium tracking-tight text-ink">{title}</h2>}
            {subtitle && <p className="mt-0.5 text-sm text-ink-soft">{subtitle}</p>}
          </div>
          {action}
        </header>
      )}
      {children}
    </section>
  )
}
