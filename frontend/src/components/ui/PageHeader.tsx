import type { ReactNode } from 'react'

export function PageHeader({
  title,
  description,
  eyebrow,
  action,
}: {
  title: string
  description?: string
  eyebrow?: string
  action?: ReactNode
}) {
  return (
    <div className="enter mb-8 flex flex-wrap items-end justify-between gap-4">
      <div>
        {eyebrow && <p className="num mb-2 text-xs uppercase tracking-[0.18em] text-primary-light">{eyebrow}</p>}
        <h1 className="text-3xl font-semibold tracking-tight text-ink sm:text-[2rem]">{title}</h1>
        {description && <p className="mt-2 max-w-2xl text-sm text-ink-soft">{description}</p>}
      </div>
      {action}
    </div>
  )
}
