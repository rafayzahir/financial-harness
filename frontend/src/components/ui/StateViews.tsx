import { AlertTriangle, Inbox, Loader2 } from 'lucide-react'
import type { ReactNode } from 'react'
import { StatusChip } from './StatusChip'

function StateShell({ icon, title, text, children }: { icon: ReactNode; title: string; text?: string; children?: ReactNode }) {
  return (
    <div className="flex flex-col items-center justify-center gap-2 rounded border border-dashed border-edge px-4 py-8 text-center">
      <div className="text-govern-light">{icon}</div>
      <p className="text-sm font-medium text-ink">{title}</p>
      {text && <p className="max-w-md text-sm text-ink-soft">{text}</p>}
      {children}
    </div>
  )
}

export function LoadingState({ label = 'Loading…' }: { label?: string }) {
  return (
    <div role="status" aria-live="polite">
      <StateShell icon={<Loader2 className="animate-spin" size={22} aria-hidden />} title={label} />
    </div>
  )
}

export function EmptyState({ title, text }: { title: string; text?: string }) {
  return <StateShell icon={<Inbox size={22} aria-hidden />} title={title} text={text} />
}

export function ErrorState({ message, onRetry }: { message: string; onRetry?: () => void }) {
  return (
    <div role="alert">
      <StateShell icon={<AlertTriangle size={22} className="text-loss" aria-hidden />} title="Something went wrong" text={message}>
        {onRetry && (
          <button type="button" onClick={onRetry} className="btn btn-primary mt-2">
            Try again
          </button>
        )}
      </StateShell>
    </div>
  )
}

/**
 * Honest placeholder used while a backend API does not exist yet.
 * The shimmering bars are decoration only. They are not data.
 */
export function ApiPendingState({ dependency }: { dependency: string }) {
  return (
    <div className="rounded border border-dashed border-edge px-4 py-6">
      <div className="mb-4 flex items-center gap-2">
        <StatusChip tone="amber" live>
          Awaiting API
        </StatusChip>
      </div>
      <div className="space-y-2.5" aria-hidden>
        <div className="skeleton h-3 w-3/4" />
        <div className="skeleton h-3 w-1/2" style={{ animationDelay: '0.2s' }} />
        <div className="skeleton h-3 w-2/3" style={{ animationDelay: '0.4s' }} />
      </div>
      <p className="mt-4 text-sm text-ink-soft">
        No data yet. This section needs: <span className="text-ink">{dependency}</span>.
      </p>
    </div>
  )
}
