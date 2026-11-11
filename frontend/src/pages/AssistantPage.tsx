import { Send } from 'lucide-react'
import { Card } from '../components/ui/Card'
import { PageHeader } from '../components/ui/PageHeader'
import { ApiPendingState } from '../components/ui/StateViews'

// Example questions from the brief. They are only suggestions to read, not AI answers.
const exampleQuestions = [
  'Analyze Apple stock.',
  'Compare Apple and Microsoft.',
  'Explain the latest company earnings.',
  'Show technical indicators for a stock.',
  'Compare two investment scenarios.',
  'Analyze my portfolio.',
  'What happens if a stock price changes by 10%?',
]

export function AssistantPage() {
  return (
    <>
      <PageHeader eyebrow="Conversation" title="AI Assistant" description="Ask stock market questions in plain language." />
      <div className="grid gap-6 xl:grid-cols-[1fr_340px]">
        <Card className="flex min-h-[440px] flex-col" delay={80}>
          <div className="flex-1" aria-live="polite">
            <ApiPendingState dependency="Danial: chat API. Hamid: AI response JSON structure" />
          </div>
          <form
            className="mt-5 flex gap-2"
            onSubmit={(e) => {
              e.preventDefault()
            }}
          >
            <label htmlFor="chat-input" className="sr-only">
              Ask a question
            </label>
            <div className="relative min-w-0 flex-1">
              <span className="num pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-primary-light" aria-hidden>
                &gt;
              </span>
              <input id="chat-input" disabled placeholder="Chat is not available yet" className="field !h-12 !pl-8" />
            </div>
            <button type="submit" disabled aria-label="Send" className="btn btn-primary !h-12 !w-12 !px-0">
              <Send size={18} />
            </button>
          </form>
        </Card>

        <Card title="Things you can ask" subtitle="Examples from the project brief" delay={140}>
          <ul className="space-y-2 text-sm text-ink-soft">
            {exampleQuestions.map((q, i) => (
              <li
                key={q}
                className="flex gap-3 rounded border border-white/5 bg-canvas/60 px-3 py-2 transition-colors hover:border-primary/30 hover:text-ink"
              >
                <span className="num text-xs text-primary-light">{String(i + 1).padStart(2, '0')}</span>
                {q}
              </li>
            ))}
          </ul>
        </Card>
      </div>
    </>
  )
}
