import { TrendingUp } from 'lucide-react'

export function Logo({ className = '' }: { className?: string }) {
  return (
    <span className={`inline-flex items-center gap-2 font-semibold tracking-tight ${className}`}>
      <span className="grid size-8 place-items-center rounded-lg bg-brand-600 text-white" aria-hidden>
        <TrendingUp size={18} />
      </span>
      <span>Financial Harness</span>
    </span>
  )
}
