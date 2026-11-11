import type { DataMeta } from '../../types/common'
import { StatusChip } from './StatusChip'

const freshnessLabel: Record<NonNullable<DataMeta['freshness']>, string> = {
  realtime: 'Real-time',
  delayed: 'Delayed data',
  historical: 'Historical data',
}

/**
 * Shown under every financial result (brief section 4).
 * It displays only what the backend actually provided. Nothing is guessed.
 */
export function DataSourceFooter({ meta }: { meta?: DataMeta }) {
  if (!meta) return null

  const items: { label: string; value: string }[] = []
  if (meta.source) items.push({ label: 'Source', value: meta.source })
  if (meta.timestamp) items.push({ label: 'As of', value: new Date(meta.timestamp).toLocaleString() })
  if (meta.reportingPeriod) items.push({ label: 'Reporting period', value: meta.reportingPeriod })
  if (meta.freshness) {
    const delay = meta.freshness === 'delayed' && meta.delayMinutes ? ` (~${meta.delayMinutes} min)` : ''
    items.push({ label: 'Data type', value: freshnessLabel[meta.freshness] + delay })
  }

  const hasNotes = (meta.assumptions?.length ?? 0) > 0 || (meta.limitations?.length ?? 0) > 0
  if (items.length === 0 && !hasNotes && !meta.isSimulation) return null

  return (
    <footer className="mt-5 space-y-3 border-t border-white/5 pt-4 text-xs text-ink-mute">
      {meta.isSimulation && (
        <StatusChip tone="amber">Simulated result · not a guaranteed return</StatusChip>
      )}
      {items.length > 0 && (
        <dl className="flex flex-wrap gap-x-6 gap-y-1.5">
          {items.map((i) => (
            <div key={i.label} className="flex gap-1.5">
              <dt className="num uppercase tracking-wider text-ink-mute">{i.label}</dt>
              <dd className="num text-ink-soft">{i.value}</dd>
            </div>
          ))}
        </dl>
      )}
      {meta.assumptions && meta.assumptions.length > 0 && (
        <div>
          <p className="num uppercase tracking-wider text-ink-soft">Assumptions</p>
          <ul className="mt-1 list-disc pl-4">
            {meta.assumptions.map((a) => (
              <li key={a}>{a}</li>
            ))}
          </ul>
        </div>
      )}
      {meta.limitations && meta.limitations.length > 0 && (
        <div>
          <p className="num uppercase tracking-wider text-ink-soft">Limitations</p>
          <ul className="mt-1 list-disc pl-4">
            {meta.limitations.map((l) => (
              <li key={l}>{l}</li>
            ))}
          </ul>
        </div>
      )}
    </footer>
  )
}
