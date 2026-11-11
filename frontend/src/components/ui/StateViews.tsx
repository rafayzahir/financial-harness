import { AlertTriangle, Inbox, Loader2, PlugZap } from 'lucide-react'
import type { ReactNode } from 'react'

function StateShell({ icon, title, text, children }: { icon: ReactNode; title: string; text?: string; children?: ReactNode }) {
  return (
    <div className="flex flex-col items-center justify-center gap-2 rounded-xl border border-dashed border-navy-600 px-4 py-8 text-center">
      <div className="text-brand-400">{icon}</div>
      <p className="text-sm font-medium text-ink-100">{title}</p>
      {text && <p className="max-w-md text-sm text-ink-500">{text}</p>}
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
          <button
            type="button"
            onClick={onRetry}
            className="mt-2 rounded-lg bg-brand-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-brand-500"
          >
            Try again
          </button>
        )}
      </StateShell>
    </div>
  )
}

/**
 * Honest placeholder used while a backend API does not exist yet.
 * It never shows fake numbers. It only says which dependency is missing.
 */
export function ApiPendingState({ dependency }: { dependency: string }) {
  return (
    <StateShell
      icon={<PlugZap size={22} aria-hidden />}
      title="Waiting for backend data"
      text={`No data yet. This section needs: ${dependency}.`}
    />
  )
}
